import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

// Create Hash
function createHash() {
  const hashKey = 'HolbertonSchools';
  const hashValues = {
    'Portland': 50,
    'Seattle': 80,
    'New York': 20,
    'Bogota': 20,
    'Cali': 40,
    'Paris': 2
  };

  for (const [field, value] of Object.entries(hashValues)) {
    client.hset(hashKey, field, value, redis.print);
  }
}

// Display Hash
function displayHash() {
  const hashKey = 'HolbertonSchools';
  client.hgetall(hashKey, (err, object) => {
    if (err) {
      console.error(err);
      return;
    }
    console.log(object);
  });
}

// Main function to run operations
function main() {
  createHash();
  setTimeout(() => {
    displayHash();
    // Close the Redis connection after displaying the hash
    setTimeout(() => client.quit(), 100);
  }, 100);
}

// Run the main function
main();
