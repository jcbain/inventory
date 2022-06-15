import express from "express";

const app = express();
const port = 5566;

(async () => {
  app.get("/dogs", (req, res) => {
    res.send("dogs");
  });
  app.listen(port, console.log(`listening on port ${port}`));
})();
