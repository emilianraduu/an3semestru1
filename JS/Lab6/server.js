const PORT = 1234;

let http = require("http");
let fs = require("fs");
let yaml = require("js-yaml");

let server = http.createServer(handleRequest);

server.listen(PORT);
console.log(`Listening on http://localhost:${PORT}`);

function handleRequest(req, res) {
  if (req.method === "GET") {
    let baseUrl = req.url.split("?")[0];
    let filename = baseUrl.split("/").pop();
    let file;
    try {
      file = fs.readFileSync(filename, "utf-8");
    } catch {
      send404(res, filename);
    }
    let doc = yaml.safeLoad(file);
    getHtmlFromYaml(res, doc);
  } else {
    send400(res);
  }
}

function getHtmlFromYaml(res, doc) {
  const htmlResponse = `
    <html>
        <body style="padding: 0; margin: 0;">
            <div style="background: green; color: white; padding: 15px; position: sticky; top: 0;">
                <h1>${doc.info.title}</h1>
                <h2>Swagger version v${doc.swagger}</h2>
                <div style='display: flex; justify-content: space-between;'>
                    <p>Email: ${doc.info.contact.email}</p>
                    <p>Description: ${doc.info.description}</p>
                    <p>Name: ${doc.info.contact.url}</p>
                    <p>Host: ${doc.host}</p>
                </div>
            </div>
                <div style="padding: 30px;">
                <h2>Models</h2>
                <div style="display: flex; flex-wrap: wrap;">
                    ${Object.keys(doc.parameters).map(param => {
                    return `
                    <div style="background: red; color: white; width: fit-content; margin-right: 15px; margin-bottom: 15px; padding: 15px;">
                        <h3>${param}</h3>
                        <h4>Reference: ${doc.parameters[param].schema ? doc.parameters[param].schema['$ref'] : '-'}</h4>
                        <h4>Description: ${doc.parameters[param].description}</h4>
                        <h4>Required: ${doc.parameters[param].required}</h4>
                    </div>`;
                    }).join('')}
                </div>
                <h1>Methods</h1>
                ${getApiMethods(doc.paths)}
            </div>
        </body>
    </html>

    `;
  res.write(htmlResponse);
  res.end();
}
function getCRUD(key){
    let methodHtml = ``
    for (let method in key){
        methodHtml+=`
        <div>
            <h2>${method}</h2>
        </div>`
    }
    return methodHtml
}
function getApiMethods(paths){
    let methodHtml = ``
    for (let key in paths){
        methodHtml +=`
        <div>
            <h5>Path: ${key}</h5>
            <div style="background: lightgrey; color: white; border-radius: 5px; padding: 15px;">
                ${getCRUD(paths[key])}
            </div>
        </div>
        `
    }
    return methodHtml
}

function send400(res) {
  const jsonResp = JSON.stringify({
    status: 400,
    reason: "Bad request: use GET only"
  });
  res.writeHead(400, {
    "Content-type": "application/json"
  });
  res.write(jsonResp);
}

function send404(res, filename) {
  const response = `<html>
    <body>
    <h2> 404 NOT FOUND </h2>
    <p> file ${filename} doesn't exist </p>
    </body>
  </html>`;
  res.writeHead(404, {
    "Content-type": "text/html"
  });
  res.end(response);
}
