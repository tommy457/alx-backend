function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  for (const jobData of jobs) {
    const job = queue.create('push_notification_code_3', jobData);
    job.save((err) => {
      if (!err) console.log(`Notification job created: ${job.id}`);
    }).on('progress', (progress, data) => {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    }).on('complete', (result) => {
      console.log(`Notification job ${job.id} completed`);
    }).on('failed', (errorMessage) => {
      console.log(`Notification job ${job.id} failed: ${errorMessage}`);
    });
  }
}

module.exports = createPushNotificationsJobs;
