DEBUG=JEKYLL_GITHUB_TOKEN=blank

default:
	@gem install jekyll bundler && bundle install

update:
	@bundle update

clean:
	@bundle exec jekyll clean

build: clean
	@${DEBUG} bundle exec jekyll build --profile --config _config.yml,.debug.yml

server: clean
	@bundle exec jekyll serve --livereload --config _config.yml,.debug.yml --host 0.0.0.0
