import { createClient } from 'redis';

createClient()
  .on('error', (err) => console.log('Redis client not connected to the server:', err.message))
  .on('connect', () => console.log('Redis client connected to the server'));
