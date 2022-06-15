import express from "express";
import axios from "axios";

const app = express();
const port = 7777;

(async () => {
  app.get("/dogs", async (req, res) => {
    const data = await axios.get("http://server:5566/dogs");
    res.send(data.data);
  });

  app.listen(port, console.log(`listening on port ${port}`));
})();
