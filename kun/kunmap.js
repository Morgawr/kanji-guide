var outb = document.getElementById('output');

const options = {
  threshold: 0,
  ignoreLocation: true,
  findAllMatches: true,
  keys: ["kun", "kanji"]
}

async function fetchData(){
   let response = await fetch('kun_map.json');
   let data = await response.json();
   return data;
}

let json_data = await fetchData();

const fuse = new Fuse(json_data, options);

document.getElementById('textbox').addEventListener('input', function(){
  let v = this.value;
  outb.innerHTML = "";

  let results = fuse.search(v);

  let output = "";
  results.forEach(function(result, index) {
    output += "<li><b>" + result.item["kun"] + "</b> → " + result.item["kanji"] + "</li>";
  })
  outb.innerHTML = output;
});

