// frontend/src/services/api.js
import axios from 'axios';
const api = axios.create({
  baseURL: 'http://localhost:8000/api',
  headers: { 'Content-Type': 'application/json' }
});
export const queryDocuments = async (question, top_k = 5) => {
  const { data } = await api.post('/query', { question, top_k });
  return data;  // { question, answer, sources, model_used }
};
export const uploadDocument = async (file) => {
  const form = new FormData();
  form.append('file', file);
  const { data } = await api.post('/upload', form, {
    headers: { 'Content-Type': 'multipart/form-data' }
  });
  return data;
};
export const reindexDocuments = () => api.post('/index');
export const listDocuments   = () => api.get('/documents').then(r => r.data)