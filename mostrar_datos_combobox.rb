require 'nokogiri'
require 'open-uri'
page = Nokogiri::HTML(open('http://www.mef.gob.pe/contenidos/tipo_cambio/tipo_cambio.php'))
page.css("select[name='nuevo_ano'] option").each do |option|
  puts option.content
end
