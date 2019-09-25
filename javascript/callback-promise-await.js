// callback
readFile(function (err, data) => {
    if(err) return console.error(err)
  console.log(data)
})

// promise
let promise = readFile()
promise.then(console.log, console.error)

// await
let data = await readFile()
console.log(contents)