import { useState } from 'react';
import SearchBar from './components/SearchBar';
import SourceList from './components/SourceList';
import { queryDocuments } from './services/api';
import './App.css';

export default function App() {
  const [result, setResult]   = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError]     = useState('');

  const handleSearch = async (question) => {
    setLoading(true);
    setError('');
    try {
      const data = await queryDocuments(question);
      setResult(data);
    } catch (e) {
      setError('Erro ao consultar. Verifique se o backend está rodando.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <header>
        <div className="logo-badge">Assistente ativo</div>
        <h1>Documentation Assistant</h1>
        <p>Consulte os documentos da empresa em linguagem natural</p>
      </header>

      <SearchBar onSearch={handleSearch} loading={loading} />

      {error && <div className="error">{error}</div>}

      {result && (
        <div className="result">
          <div className="answer">
            <div className="answer-header">
              <div className="answer-icon">✦</div>
              <h2>Resposta</h2>
            </div>
            <p>{result.answer}</p>
            <small>Modelo: {result.model_used}</small>
          </div>
          <SourceList sources={result.sources} />
        </div>
      )}
    </div>
  );
}