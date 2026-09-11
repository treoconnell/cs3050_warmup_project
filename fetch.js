import fs from 'node:fs';

function smartsplit(string){
    let in_quotes = false
    let indices = []
    for(let i = 0; i<string.length; i++){
        let char = string[i]
        if (char == "\""){
            in_quotes = !in_quotes
            string = string.slice(0, i) + string.slice(i + 1);
            char = string[i]
        }
        if(char == "," && !in_quotes){
            indices.push(i)
        }
    }
    let ret = [string.slice(0, indices[0])]
    for(let i = 1; i<indices.length; i++){
        ret.push(string.slice(indices[i-1]+1, indices[i]))
    }
    ret.push(string.slice(indices[indices.length-1]+1))
    return ret;
}

try {
  const lines = fs.readFileSync('top_100_movies_full_best_effort.csv', 'utf8').trim().split('\n');
  let names = ["title", "year", "rating", "box_office"]
  let indices = [1, 2, 7, 12]

  // Title rating year box office
  let items = []
  for(let i = 1; i<lines.length; i++){
    let item = {};
    const line = smartsplit(lines[i]);
    // console.error(line[1])
    if (line[1].includes('(dup')){
        continue
    }
    for(let j = 0; j<names.length; j++){
        if(line[indices[j]] != '')
            item[names[j]] = line[indices[j]]
    }
    items.push(item)
  }
  console.log(items);
  fs.writeFileSync("top_movies.json", JSON.stringify(items, null, 2))
//   console.log(items.length)
} catch (err) {
  console.error(err);
}
