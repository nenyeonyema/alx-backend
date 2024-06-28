// Import necessary modules using ES6 syntax
import { createClient, print } from 'redis';

// Create a Redis client
const client = createClient();

// Handle successful connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Handle connection error
client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

// Connect to the Redis server
client.connect();

// Function to set a new key-value pair in Redis
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print); // Using redis.print for confirmation
}

// Function to display the value for a given key from Redis
function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, result) => {
    if (err) {
      console.error(`Error getting value for ${schoolName}: ${err.message}`);
    } else {
      console.log(result);
    }
  });
}

// Call the functions
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
