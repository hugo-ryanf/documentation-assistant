import { useState } from 'react';

export default function SearchBar({ onSearch, loading }) {
  const [question, setQuestion] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (question.trim()) onSearch(question.trim());
  };

  return (
    <form onSubmit={handleSubmit}>
      <div className="search-container">
        <input
          className="search-input"
          type="text"
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          placeholder="Faça uma pergunta sobre os documentos..."
          disabled={loading}
        />
        <button
          className={`search-btn${loading ? ' loading' : ''}`}
          type="submit"
          disabled={loading || !question.trim()}
        >
          {loading ? 'Buscando' : 'Perguntar'}
        </button>
      </div>
    </form>
  );
}