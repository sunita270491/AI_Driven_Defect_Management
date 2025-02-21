import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [defects, setDefects] = useState([]);
  const [selectedDefect, setSelectedDefect] = useState(null);
  const [suggestions, setSuggestions] = useState({});

  useEffect(() => {
    fetchDefects();
  }, []);

  const fetchDefects = async () => {
    const response = await axios.get('https://api.mocked_defect_tool.com/defects');
    setDefects(response.data);
  };

  const handleDefectClick = async (defect) => {
    setSelectedDefect(defect);
    const response = await axios.post('http://localhost:8000/suggest', defect);
    setSuggestions(response.data);
  };

  return (
    <div className="App">
      <h1>AI-Driven Defect Management</h1>
      <div className="defect-list">
        {defects.map((defect) => (
          <div key={defect.id} onClick={() => handleDefectClick(defect)}>
            <h2>Defect ID: {defect.id}</h2>
            <p>{defect.description}</p>
          </div>
        ))}
      </div>
      {selectedDefect && (
        <div className="defect-details">
          <h2>Defect Details</h2>
          <p>ID: {selectedDefect.id}</p>
          <p>Description: {selectedDefect.description}</p>
          <p>Steps to Reproduce: {selectedDefect.steps_to_reproduce}</p>
          <p>Expected Result: {selectedDefect.expected_result}</p>
          <p>Actual Result: {selectedDefect.actual_result}</p>
          <h3>AI Suggestions</h3>
          <p>Description: {suggestions.description}</p>
          <p>Steps to Reproduce: {suggestions.steps_to_reproduce}</p>
        </div>
      )}
    </div>
  );
}

export default App;