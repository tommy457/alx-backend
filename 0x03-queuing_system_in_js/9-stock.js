import express from 'express';
import { promisify } from 'util';
import { createClient } from 'redis';

const app = express();
const port = 1245;

const client = createClient()
  .on('error', (err) => console.log('Redis client not connected to the server:', err.message))
  .on('connect', () => console.log('Redis client connected to the server'));

app.listen(port, () => {});

const get = promisify(client.get).bind(client);

const listProducts = [
  {
    itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4,
  },
  {
    itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10,
  },
  {
    itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2,
  },
  {
    itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5,
  },
];

function getItemById(id) {
  return listProducts.filter((item) => item.itemId === id)[0];
}

function reserveStockById(itemId, stock) {
  client.set(itemId, stock);
}

async function getCurrentReservedStockById(itemId) {
  return get(itemId);
}

app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const item = getItemById(itemId);
  if (!item) {
    res.json({ status: 'Product not found' });
  }
  const stock = await getCurrentReservedStockById(itemId);
  const resItem = {
    itemId: item.itemId,
    itemName: item.itemName,
    price: item.price,
    initialAvailableQuantity: item.initialAvailableQuantity,
    currentQuantity: stock ? parseInt(stock, 10) : item.initialAvailableQuantity,
  };
  res.json(resItem);
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const stock = await getCurrentReservedStockById(itemId);
  const item = getItemById(parseInt(itemId, 10));

  if (!item) {
    res.json({ status: 'Product not found' });
  }
  if (stock < 1) {
    res.send({ status: 'Not enough stock available', itemId });
  }
  reserveStockById(itemId, stock - 1);
  res.send({ status: 'Reservation confirmed', itemId });
});
