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

// Function to create a hash and store values in Redis
function createHash() {
  client.hset('HolbertonSchools', 'Portland', 50, print); // Set value for Portland
  client.hset('HolbertonSchools', 'Seattle', 80, print); // Set value for Seattle
  client.hset('HolbertonSchools', 'New York', 20, print); // Set value for New York
  client.hset('HolbertonSchools', 'Bogota', 20, print); // Set value for Bogota
  client.hset('HolbertonSchools', 'Cali', 40, print); // Set value for Cali
  client.hset('HolbertonSchools', 'Paris', 2, print); // Set value for Paris
}

// Function to display the hash values stored in Redis
function displayHash() {
  client.hgetall('HolbertonSchools', (err, result) => {
    if (err) {
      console.error(`Error retrieving hash: ${err.message}`);
    } else {
      console.log(result); // Print the hash values
    }
  });
}

// Call the functions
createHash();
displayHash();

