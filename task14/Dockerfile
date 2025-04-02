FROM nginx:1.27.4-alpine
RUN mkdir -p /var/www/html
COPY html/ /var/www/html
COPY nginx.conf /etc/nginx/
RUN mkdir -p /etc/letsencrypt/live/trainee4.com
COPY fullchain.pem privkey.pem /etc/letsencrypt/live/trainee4.com
EXPOSE 80 443 8081 8082
CMD ["nginx", "-g", "daemon off;"] 
