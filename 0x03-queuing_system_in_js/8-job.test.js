import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', () => {
  let queue;

  beforeEach(() => {
    queue = kue.createQueue();
    queue.testMode.enter(); // Enter test mode
  });

  afterEach(() => {
    queue.testMode.clear(); // Clear the queue after each test
    queue.testMode.exit(); // Exit test mode
  });

  it('should throw an error if jobs is not an array', () => {
    expect(() => createPushNotificationsJobs('not an array', queue)).to.throw('Jobs is not an array');
  });

  it('should create jobs in the queue', () => {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 4562 to verify your account'
      }
    ];

    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].data).to.deep.equal({
      phoneNumber: '4153518780',
      message: 'This is the code 1234 to verify your account'
    });
    expect(queue.testMode.jobs[1].data).to.deep.equal({
      phoneNumber: '4153518781',
      message: 'This is the code 4562 to verify your account'
    });
  });

  it('should log appropriate messages for job events', (done) => {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      }
    ];

    const consoleLog = console.log;
    let logOutput = [];
    console.log = (message) => {
      logOutput.push(message);
    };

    createPushNotificationsJobs(jobs, queue);

    const job = queue.testMode.jobs[0];
    job.complete();
    job.failed('Failed to send message');
    job.progress(50);

    setTimeout(() => {
      expect(logOutput).to.include(`Notification job created: ${job.id}`);
      expect(logOutput).to.include(`Notification job ${job.id} completed`);
      expect(logOutput).to.include(`Notification job ${job.id} failed: Failed to send message`);
      expect(logOutput).to.include(`Notification job ${job.id} 50% complete`);

      console.log = consoleLog;
      done();
    }, 50);
  });
});

