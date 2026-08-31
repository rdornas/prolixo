/** @type {import('next').NextConfig} */
const nextConfig = {
  async rewrites() {
    const apiPort = process.env.API_PORT || '8000';
    return [
      {
        source: '/api/:path*',
        destination: process.env.NODE_ENV === 'development'
          ? `http://localhost:${apiPort}/api/:path*`
          : '/api/:path*',
      },
    ];
  },
};

module.exports = nextConfig;
