var outb = document.getElementById('output');

const options = {
  threshold: 0,
  ignoreLocation: true,
  findAllMatches: true,
  keys: ["kun_no_okurigana", "kanji", "kanji_ext"]
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
    output += "<li><b>" + result.item["kun"] + "</b> → " + result.item["kanji_oku"];
    if (result.item["kanji_ext_oku"].length > 0)
      output += " (外) " + result.item["kanji_ext_oku"];
    output += "</li>";
  })
  outb.innerHTML = output;
});

