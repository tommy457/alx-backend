import { createClient, print } from 'redis';

const client = createClient()
  .on('error', (err) => console.log('Redis client not connected to the server:', err.message))
  .on('connect', () => console.log('Redis client connected to the server'));

const hash = {
  Portland: 50,
  Seattle: 80,
  'New York': 20,
  Bogota: 20,
  Cali: 40,
  Paris: 2,

};

for (const key in hash) {
  client.hmset('HolbertonSchools', key, hash[key], print);
}

client.hgetall('HolbertonSchools', (err, res) => {
  console.log(res);
});
