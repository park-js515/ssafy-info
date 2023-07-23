import express from "express";

const app = express();
app.set("view engine", "pug");
app.set("views", __dirname + "/views"); // __dirname은 현재 파일의 위치를 나타내는 변수
app.use("/public", express.static(__dirname + "/public")); // 미들웨어의 역할? Frontend에서 구동되는 파일들

app.get("/", (req, res) => res.render("home"));
app.get("/*", (req, res) => res.redirect("/"));

console.log(__dirname)
const handleListen = () => console.log(`Listening on http://localhost:3000`);
app.listen(3000, handleListen);
