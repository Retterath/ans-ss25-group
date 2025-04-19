"""
 Copyright (c) 2025 Computer Networks Group @ UPB

 Permission is hereby granted, free of charge, to any person obtaining a copy of
 this software and associated documentation files (the "Software"), to deal in
 the Software without restriction, including without limitation the rights to
 use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
 the Software, and to permit persons to whom the Software is furnished to do so,
 subject to the following conditions:

 The above copyright notice and this permission notice shall be included in all
 copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
 FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
 COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
 IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
 CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
 """

#!/usr/bin/python

from mininet.topo import Topo

class BridgeTopo(Topo):
    "Creat a bridge-like customized network topology according to Figure 1 in the lab0 description."

    def __init__(self):

        Topo.__init__(self)

        #add hosts
        h1 = Topo.addHost(self, name="h1")
        h2 = Topo.addHost(self, name="h2")
        h3 = Topo.addHost(self, name="h3")
        h4 = Topo.addHost(self, name="h4")

        #add switches
        s1 = Topo.addSwitch(self, name="s1")
        s2 = Topo.addSwitch(self, name="s2")

        #add links
        e1 = Topo.addLink(self, node1=h1, node2=s1, bw=15, delay="10ms")
        e2 = Topo.addLink(self, node1=h2, node2=s1, bw=15, delay="10ms")
        e3 = Topo.addLink(self, node1=h3, node2=s2, bw=15, delay="10ms")
        e4 = Topo.addLink(self, node1=h4, node2=s2, bw=15, delay="10ms")
        e5 = Topo.addLink(self, node1=s1, node2=s2, bw=20, delay="45ms")

topos = {'bridge': (lambda: BridgeTopo())}
