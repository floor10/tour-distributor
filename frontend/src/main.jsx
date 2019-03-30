import * as React from "react";
import * as ReactDOM from "react-dom";
// import { Provider } from 'react-redux';
// import { BrowserRouter } from "react-router-dom";

import { App } from "./app";
// import { configureStore } from "app/store"

ReactDOM.render(
  <App />
//   <Provider store={configureStore()}>
//     <BrowserRouter>
//       <App />
//     </BrowserRouter>
//   </Provider>
  ,
  document.getElementById("root")
);
