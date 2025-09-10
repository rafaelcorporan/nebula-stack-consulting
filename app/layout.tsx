import type { Metadata } from 'next';
import { Inter } from 'next/font/google';
import './globals.css';
import ErrorBoundary from '@/components/ErrorBoundary';

const inter = Inter({ subsets: ['latin'] });

// Viewport configuration
export const viewport = {
  width: 'device-width',
  initialScale: 1,
  themeColor: '#0284c7', // sky-600
};

export const metadata: Metadata = {
  title: 'Nebula Stack Consulting',
  description: 'Enterprise-grade cloud, infrastructure, and software development — delivered with precision.',
  metadataBase: new URL(process.env.NEXT_PUBLIC_SITE_URL || 'http://localhost:3000'),
  openGraph: {
    title: 'Nebula Stack Consulting',
    description: 'Enterprise-grade cloud, infrastructure, and software development — delivered with precision.',
    type: 'website',
    locale: 'en_US',
    url: '/',
    siteName: 'Nebula Stack Consulting',
  },
  twitter: {
    card: 'summary_large_image',
    title: 'Nebula Stack Consulting',
    description: 'Enterprise-grade cloud, infrastructure, and software development — delivered with precision.',
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className="h-full bg-white">
      <body className={`${inter.className} min-h-full`}>
        <ErrorBoundary>
          {children}
        </ErrorBoundary>
      </body>
    </html>
  );
}
