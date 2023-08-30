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


function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (err, reply) => {
    if (err) {
      console.error('Error setting key:', err); 
    } else {
      console.log('Reply:', reply);
    }
  });
}

function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, value) => {

    if (err) {
      console.error('Error getting value:', err);
    } else {
      console.log(`${value}`);
    }
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
