import scrapy

class brasil_mineral(scrapy.Spider):
    name = "news"
    allowed_domains = ["brasilmineral.com.br/noticias"]
    start_urls = ["https://www.brasilmineral.com.br/noticias"]

    def parse(self, response):
        # Captura todos os containers com a classe "teaser__content"
        teasers = response.css('div.teaser__content')

        for teaser in teasers:
            # Captura o título da notícia
            title = teaser.css('h2.teaser__headline span.field.field--name-title.field--type-string.field--label-hidden::text').get()

            # Captura a data da notícia
            date = teaser.css('span.date::text').get()

            # Captura o resumo da notícia
            summary = teaser.css('div.field.field--name-field-teaser-text.field--type-string-long.field--label-hidden.field__item::text').get()

            # Verifica se todos os dados foram encontrados e retorna
            if title and date and summary:
                yield {
                    'title': title.strip(),
                    'date': date.strip(),
                    'summary': summary.strip()
                }
