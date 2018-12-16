
### How to: Install Go 1.11.2 on Ubuntu
https://medium.com/@patdhlk/how-to-install-go-1-9-1-on-ubuntu-16-04-ee64c073cd79

$ sudo snap install go --classic

$ go version
go version go1.11.2 linux/amd64

$ which go
/snap/bin/go

  $ snap find go
  $ snap list
  $ sudo snap remove go
  $ sudo snap install go


### install go1.9.7

https://golang.org/doc/install?download=go1.9.7.linux-amd64.tar.gz

  $ sudo tar -C /usr/local -xzf go1.9.7.linux-amd64.tar.gz

* test
create $HOME/go/src/hello/hello.go
  $ go run $HOME/go/src/hello/hello.go

* build
  $ cd $HOME/go/src/hello
  $ go build
  $ ./hello

* install
  $ go install
  $ ~/go/bin/hello

### install Igo - go kernel for Jupyter
* Interactive Go programming with Jupyter
https://github.com/yunabe/lgo

~/go/src/github.com/yunabe/lgo/examples
~/go/notebooks


### Learn go
* https://gobyexample.com/
* https://www.tutorialspoint.com/go/go_logical_operators.htm
* https://github.com/a8m/go-lang-cheat-sheet

$ go get github.com/mmcgrana/gobyexample    # git url without prefix=https:// and suffix=.git


### go commands

* list src repo
  $ cd $HOME/go/src
  $ go list ./...
