function getScoreClass(score) {
  if (score >= 0.7) return 'high';
  return 'medium';
}

function SourceCard({ source }) {
  const scorePercent = Math.round((source.score ?? 0) * 100);
  const cls = getScoreClass(source.score ?? 0);
  // backend retorna: content, source, page, score
  const excerpt = source.content ?? source.excerpt;
  const filename = source.source ?? source.file;

  return (
    <div className="source-card">
      <div className="source-header">
        <div className="source-file-icon">📄</div>
        <span className="source-file">{filename}</span>
        {source.page && (
          <span className="source-page">p. {source.page}</span>
        )}
        <span className={`source-score ${cls}`}>
          <span className="score-bar">
            <span
              className={`score-fill ${cls}`}
              style={{ width: `${scorePercent}%` }}
            />
          </span>
          {scorePercent}%
        </span>
      </div>
      {excerpt && (
        <p className="source-excerpt">{excerpt}</p>
      )}
    </div>
  );
}

export default function SourceList({ sources }) {
  if (!sources?.length) return null;

  return (
    <div className="sources">
      <h3>
        Fontes utilizadas
        <span className="sources-count">{sources.length}</span>
      </h3>
      {sources.map((src, i) => (
        <SourceCard key={i} source={src} />
      ))}
    </div>
  );
}