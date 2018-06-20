// MIT License
// conceived and coded by Jason Mitchell, MD, MS
// Version 0.1
// 2018-06-15


'use strict';

const express = require( 'express' );

const path = require( 'path' );

const bodyParser = require( 'body-parser' );

const app = express();

var instructions = '{"command": "stay"}';

// support encoded bodies
app.use( bodyParser.urlencoded( {extended: false } ) );

// support json encoded bodies
app.use( bodyParser.json() );


// [START rover]
// control rover robot

// Use the built-in express middleware for serving static files from "./robot"
app.use( '/static', express.static( 'robot' ) );

//allow express to access our root html ( index.html ) file
app.get( '/', function( req, res ) {
	res.sendFile( __dirname + '/robot/control_UI.html' );
} );

app.route( '/instructions' )
  .get(function ( req, res ) {  // service to read control instructions
    res.status( 200 ).send( instructions );
  } )
  .post(function ( req, res ) {  // service to write control instructions
  	instructions = req.body;	
    res.status( 200 ).send( instructions );
  } );
  

// [END rover]

if ( module === require.main ) {
  // [START server]
  // Start the server
  const server = app.listen(process.env.PORT || 8080, () => {
    const port = server.address().port;
    console.log( `App listening on port ${port}` );
  } );
  // [END server]
}

module.exports = app;
