const proxy = require("express-http-proxy");
const app = require("express")();

app.use("/proxy", proxy("http://localhost:8080/"));

app.use("/", (req, res) => {
  console.log(req);
  res.send("hello");
});

app.listen(8080, () => console.log("listening on port 8080"));
