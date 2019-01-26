const express = require('express');
const ejs = require('ejs')
const port = process.env.PORT || 3000;
const app = express();
app.set('view engine','ejs')
app.get('/',(req,res)=>{
    res.render('index');
});
app.get('/login',(req,res)=>{
    res.render('login');
});
app.get('/dashboard',(req,res)=>{
    res.render('dashboard')
})
app.get('/logout',(req,res)=>{
    res.render('logout');
})
app.listen(port,()=>{
    console.log(`server started on port:${port}`)
});