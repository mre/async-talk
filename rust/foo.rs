#[prelude_import]
use std::prelude::v1::*;
#[macro_use]
extern crate std;

async fn say_hi() -> ::std::future::from_generator(
            println!("Hello world! 🤖");
    }})

async fn main() {
let t = match say_hi() {
loop {
    match ::std::future::poll_with_tls_context(
        unsafe { <::std::pin::Pin>::new_unchecked(&mut pinned) }) {
            ::std::task::Poll::Ready(result) => break result,
            ::std::task::Poll::Pending => { }
        }
    yield ();
    },
t
}
})
runtime::raw::enter(runtime::native::Native,
::std::future::from_generator(||
{
match main()
{
mut pinned
=>
loop 
{
match ::std::future::poll_with_tls_context(unsafe
{
<::std::pin::Pin>::new_unchecked(&mut pinned)
})
{
::std::task::Poll::Ready(result) => break result,
 ::std::task::Poll::Pending => { }
}
yield
();
},
}
}))
}

