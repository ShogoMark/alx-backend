import redis from 'redis';
import 'core-js/stable';
import 'regenerator-runtime/runtime';

// create a Redis client
const client = redis.createClient();

// Handle the connection event
client.on('connect', () => {
  console.error('Redis client connected to the server');
});

// Handle the error
client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});

client.set('key', 'value', (err, reply) => {
if (err) {
  console.error('Error setting value:', err);
} else {
  console.log('Value set:', reply);
 }
});

client.get('key', (err, value) => {
  if (err) {
    console.error('Error getting value:', err);
 } else {
     console.log('Retrieved value:', value);
     client.quit();
}
});
