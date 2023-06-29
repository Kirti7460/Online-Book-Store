import axios from 'axios';

const baseURL = 'http://localhost:3000'; // Replace with your backend server URL

// Function to fetch books from the backend
export const fetchBooks = async () => {
  try {
    const response = await axios.get(`${baseURL}/api/books`);
    return response.data;
  } catch (error) {
    throw new Error('Failed to fetch books');
  }
};

// Function to search books by title, author, or category
export const searchBooks = async (query) => {
  try {
    const response = await axios.get(`${baseURL}/api/books/search`, {
      params: { query },
    });
    return response.data;
  } catch (error) {
    throw new Error('Failed to search books');
  }
};

// Function to filter books by genre, price range, etc.
export const filterBooks = async (filters) => {
  try {
    const response = await axios.get(`${baseURL}/api/books/filter`, {
      params: filters,
    });
    return response.data;
  } catch (error) {
    throw new Error('Failed to filter books');
  }
};

// Function to add a book to the shopping cart
export const addToCart = async (bookId) => {
  try {
    const response = await axios.post(`${baseURL}/api/cart`, { bookId });
    return response.data;
  } catch (error) {
    throw new Error('Failed to add to cart');
  }
};

// Function to place an order
export const placeOrder = async (cartItems) => {
  try {
    const response = await axios.post(`${baseURL}/api/orders`, { cartItems });
    return response.data;
  } catch (error) {
    throw new Error('Failed to place order');
  }
};
