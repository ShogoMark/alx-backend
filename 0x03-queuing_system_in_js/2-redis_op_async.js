import redis from 'redis';
import 'core-js/stable';
import 'regenerator-runtime/runtime';
import { promisify } from 'util';


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

const getAsync = promisify(client.get).bind(client);

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (err, reply) => {
    if (err) {
      console.error('Error setting value:', err);
    } else {
      console.log('Reply:', reply);
    }
  });
}

async function displaySchoolValue(schoolName) {
  try {
    const value = await getAsync(schoolName);
    if (value !== null) {
      console.log(value);
    } else {
      console.log(`${schoolName} not found.`);
    }
  } catch (err) {
    console.error('An error occurred:', err);
  }
}


displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
