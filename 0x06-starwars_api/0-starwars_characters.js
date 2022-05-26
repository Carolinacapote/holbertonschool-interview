#!/usr/bin/node
const args = process.argv;
const request = require('request');
const API = `https://swapi-api.hbtn.io/api/films/${args[2]}`;

// Call the Starwars API
request.get(API, async (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const characters = JSON.parse(body).characters;
    for (let i = 0; i < characters.length; i++) {
      await getCharacterName(characters[i]);
    }
  }
});

/** Calls the API to get the character info */
function getCharacterName (character) {
  return new Promise((resolve, reject) => {
    request.get(character, (error, response, body) => {
      if (error) {
        console.error(error);
        reject(error);
      } else {
        const characterInfo = JSON.parse(body);
        console.log(characterInfo.name);
        resolve(true);
      }
    });
  });
}
