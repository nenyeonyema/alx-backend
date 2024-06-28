// Import necessary modules using ES6 syntax
import { createClient, print } from 'redis';
import { promisify } from 'util';

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

// Promisify the get method of the Redis client
const getAsync = promisify(client.get).bind(client);

// Function to set a new key-value pair in Redis
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print); // Using redis.print for confirmation
}

// Modified function to display the value for a given key from Redis using async/await
async function displaySchoolValue(schoolName) {
  try {
    const result = await getAsync(schoolName);
    console.log(result);
  } catch (err) {
    console.error(`Error getting value for ${schoolName}: ${err.message}`);
  }
}

// Call the functions
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
