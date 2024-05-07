import kue from 'kue';

const blacklistedPhoneNumbers = ['4153518780', '4153518781'];
const queue = kue.createQueue();

function sendNotification(phoneNumber, message, job, done) {
  if (blacklistedPhoneNumbers.includes(phoneNumber)) {
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }
  job.progress(50, 100);
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

  return done();
}

queue.process('push_notification_code_2', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
