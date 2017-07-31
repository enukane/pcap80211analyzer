#!/usr/bin/env ruby

require 'ouisearch/version'
require 'optparse'
require 'faraday'

class OuiSearch
  #URL="http://standards-oui.ieee.org/oui.txt"
  URL="http://linuxnet.ca/ieee/oui.txt"
  #URLHOST="http://standards-oui.ieee.org"
  URLHOST="http://linuxnet.ca/"
  #URLPATH="/oui.txt"
  URLPATH="/ieee/oui.txt"
  CACHE="#{ENV['HOME']}/.oui"
  REG=/^\s*(..)-(..)-(..)\s+\(hex\)\s+(.+)$/

  def initialize args={}
    @reload = args[:reload] || false
    @debug = args[:debug] || false
    @ouis = nil
    fetch_cache
    load_cache
  end

  def execute oui
    if oui.length != 8
      return "<UNKNOWN>"
    end
    oui = oui.upcase
    octet0 = oui[0..1].hex & 0xfd
    octet0_str = octet0.to_s(16)
    if octet0 < 16
      octet0_str = "0" + octet0_str
    end
    oui = octet0_str + ":" + oui[3..7]

    vendor = @ouis[oui.upcase]
    if vendor
      return vendor.strip
    else
      return "<UNKNOWN>"
    end
  end

  def fetch_cache
    if File.exists?(CACHE) and @reload == false
      # nothing to do
      return
    end

    if @reload
      dprint "force cache update ($HOME/.oui) ...\n"
    else
      dprint "no cache ($HOME/.oui) found. creating cache ...\n"
    end

    File.open(CACHE, "w") do |f|
      @ouis = http_get_ouis()
      f.write(Marshal.dump(@ouis))
    end

    dprint "cache created (#{@ouis.length} entries)\n"
  end

  def http_get_ouis
    ouis = {}
    conn = Faraday.new(:url => URLHOST)
    response = conn.get(URLPATH)
    raise "failed to fetch oui" if response.status != 200
    response.body.split("\n").each do |line|
      match = line.match(REG)
      next unless match
      oui = match[1] + ":" + match[2] + ":" + match[3]
      vendor = match[4]
      ouis[oui.upcase] = vendor
    end
    return ouis
  end

  def load_cache
    return @ouis if @ouis # already fetched
    File.open(CACHE, "r") do |f|
      @ouis = Marshal.load(f.read)
    end
    dprint "cache reloading done (#{@ouis.length} entries)\n"
  end

  def dprint str
    return nil unless @debug
    print "#{str}\n"
  end
end

def usage
  print "ouisearch [-d] [-r] XX:XX:XX\n"
  exit 1
end

if __FILE__ == $0
  opt = OptionParser.new
  OPTS={}
  opt.on('-r') {|v| OPTS[:reload] = true }
  opt.on('-d') {|v| OPTS[:debug] = true }
  opt.on('-h') {|v| usage }
  opt.parse!(ARGV)

  addr = ARGV.shift
  usage if addr == nil

  begin
    ouisearch = OuiSearch.new(OPTS)
  rescue => e
    print e.message
    exit 1
  end
  print "#{ouisearch.execute(addr)}\n"

  exit 0
end
