import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Header from './components/Header';
import NavigationBar from './components/Navbar';
import Home from './components/Home';
import Services from './components/Services';
import About from './components/About';
import Contact from './components/Contact';
import Footer from './components/Footer';

const App = () => (
  <Router>
    <div>
      <NavigationBar />
      <Header />
      <Routes>
        <Route exact path="/" element={<Home />} />
        <Route path="/services" element={<Services />} />
        <Route path="/about" element={<About />} />
        <Route path="/contact" element={<Contact />} />
      </Routes>
      <Footer />
    </div>
  </Router>
);

export default App;