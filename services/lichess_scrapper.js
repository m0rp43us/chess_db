const axios = require('axios');
const mongoose = require("mongoose");
require('dotenv').config()


const PuzzleSchema = new mongoose.Schema({
    id : {
        type : String,
        required : true,
    },
    rating : {
        type : Number,
        required : true
    },
    pgn : {
        type : String,
        required : true
    },
    solution : {
        type : Array,
        required: true 
    },
    tags : {
        type : Array,
        required : true,
    }
});

mongoose.connect(process.env.DB_URI,{useNewUrlParser:true,useUnifiedTopology:true});
const db = mongoose.connection;
db.on("error",(error) => {console.log(error)});
db.once("open",() => {console.log('connected to the db')});



var config = {
  method: 'post',
  url: 'https://lichess.org/training/complete/mix/r2YIi',
  headers: { 
    'Accept': 'application/vnd.lichess.v5+json', 
    'sec-fetch-site': 'same-origin', 
    'sec-fetch-mode': 'cors', 
    'origin': 'https://lichess.org', 
    'referer': 'https://lichess.org/training'
  }
};

getData = async () => {
    axios(config)
    .then(async function (response) {
    var puzzle = new PuzzleSchema({
        'id' : response.data.next.puzzle.id,
        'rating' : response.data.next.puzzle.rating,
        'pgn' : response.data.next.game.pgn,
        'solution' : response.data.next.puzzle.solution,
        'tags' : response.data.next.puzzle.themes
    });
    console.log(puzzle);
    puzzle.save()
    //await sleep(100)
    console.log(puzzle);
    
})
.catch(function (error) {
  console.log(error);
});
}

(async () => { while(true){
    await getData();
};})();