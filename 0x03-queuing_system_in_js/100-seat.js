import express from 'express';
import { promisify } from 'util';
import { createQueue } from 'kue';
import { createClient } from 'redis';

const app = express();
const port = 1245;
const queue = createQueue();

const client = createClient()
  .on('error', (err) => console.log('Redis client not connected to the server:', err.message))
  .on('connect', () => console.log('Redis client connected to the server'));

app.listen(port, () => {});

const get = promisify(client.get).bind(client);
let reservationEnabled = true;

function reserveSeat(number) {
  client.set('available_seats', number);
}

async function getCurrentAvailableSeats() {
  const seats = await get('available_seats');
  return seats;
}

app.get('/available_seats', async (req, res) => {
  const availableSeats = await getCurrentAvailableSeats();
  res.send({ numberOfAvailableSeats: availableSeats });
});

app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    res.send({ status: 'Reservation are blocked' });
    return;
  }
  const job = queue.create('reserve_seat', { seat: 1 }).save((error) => {
    if (error) {
      res.send({ status: 'Reservation failed' });
    } else {
      res.send({ status: 'Reservation in process' });
      job.on('complete', () => {
        console.log(`Seat reservation job ${job.id} completed`);
      }).on('failed', (error) => {
        console.log(`Seat reservation job ${job.id} failed: ${error}`);
      });
    }
  });
});

app.get('/process', (req, res) => {
  res.send({ status: 'Queue processing' });
  queue.process('reserve_seat', async (job, done) => {
    const seat = Number(await getCurrentAvailableSeats());
    if (seat === 0) {
      reservationEnabled = false;
      done(Error('Not enough seats available'));
    } else {
      reserveSeat(seat - 1);
      done();
    }
  });
});

reserveSeat(50);
