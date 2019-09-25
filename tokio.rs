extern crate tokio;

use tokio::prelude::{AsyncRead, Future};

fn main() {
    let task = tokio::fs::File::open("foo.txt")
        .and_then(|mut file| {
            let mut contents = vec![];
            file.read_buf(&mut contents).map(|res| {
                println!("{:?}", res);
            })
        })
        .map_err(|err| eprintln!("IO error: {:?}", err));
    tokio::run(task);
}
