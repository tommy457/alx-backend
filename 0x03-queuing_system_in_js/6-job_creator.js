import kue from 'kue';

const queue = kue.createQueue();

const jobData = {
  phoneNumber: '123-456-798',
  message: 'message',
};
const job = queue.create('push_notification_code', jobData);

job.save((err) => {
  if (!err) console.log(`Notification job created: ${job.id}`);
}).on('complete', (result) => {
  console.log('Notification job completed');
}).on('failed', (errorMessage) => {
  console.log('Notification job failed');
});
