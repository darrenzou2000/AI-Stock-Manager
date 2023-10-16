
import React from "react";

import { BrowserRouter,Routes ,Route } from "react-router-dom";

import Home from "./pages/Home/Home";
import Auth from "./pages/Auth/Auth";
const App = () => {

  return (
    <BrowserRouter>
        <Navbar/>
        <Routes >
          <Route path="/" exact element={<Home/>}/>
          <Route path="/auth" exact element={<Auth/>}/>
        </Routes>
  </BrowserRouter>
  )
}//notes 12 on xs means full width on mobile devices

export default App