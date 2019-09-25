use futures::prelude::*;
use runtime::fs::File;

fn main() {
let f = file::open("foo.txt").await?;
let mut buffer = Vec::new();
let contents = f.read_to_end(&mut buffer).await?;
println!("{:?}", contents);
}
