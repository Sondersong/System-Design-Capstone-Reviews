const express = require("express");
const path = require("path");
const { Sequelize } = require('sequelize')

const sequelize = new Sequelize('postgres://user:pass@example.com:5432/dbname')

let app = express();

app.use(express.json());
app.use(express.static(path.join(__dirname, "../client/dist")));

app.get("/test1", (req, res) => {
  res.json(JSON.stringify({test: 'worked'}));
  res.send();
});

let port = 3001;
app.listen(port, function () {
  console.log(`listening on port ${port}`);
});
