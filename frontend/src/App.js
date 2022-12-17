import './App.css';
import {
  BrowserRouter as Router,
  Routes,
  Route
} from 'react-router-dom'

import Recipes from './pages/Recipes'
import Recipe from './pages/Recipe'
import Layout from './components/Layout'

function App() {
  return (
    <Router>
      <Layout>
        <Routes>
          <Route path={'/'} element={<Recipes/>} exact />
          <Route path={'/:id'} element={<Recipe/>} />
        </Routes>
      </Layout>
    </Router>
  );
}

export default App;