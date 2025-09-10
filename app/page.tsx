'use client';

import { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import dynamic from 'next/dynamic';
import { Button } from '@/components/ui/Button';
import LoadingSpinner from '@/components/LoadingSpinner';

// Import the modal with SSR disabled
const QuoteEstimatorModal = dynamic(
  () => import('@/components/QuoteEstimator/QuoteEstimatorModal'),
  { 
    ssr: false,
    loading: () => <LoadingSpinner size="md" />
  }
) as any; // Temporary type assertion to bypass TypeScript error

// Create a dynamic import for the 3D background with SSR disabled
const ThreeDBackground = dynamic(
  () => import('@/components/ThreeDBackground'),
  { ssr: false }
);

export default function Home() {
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [hasMounted, setHasMounted] = useState(false);
  const [prefersReducedMotion, setPrefersReducedMotion] = useState(true); // Default to true to match SSR

  // This effect only runs on the client
  useEffect(() => {
    setHasMounted(true);
    const mediaQuery = window.matchMedia('(prefers-reduced-motion: reduce)');
    setPrefersReducedMotion(mediaQuery.matches);
    
    const handler = (e: MediaQueryListEvent) => setPrefersReducedMotion(e.matches);
    mediaQuery.addEventListener('change', handler);
    return () => mediaQuery.removeEventListener('change', handler);
  }, []);

  // Show loading state until client-side hydration is complete
  if (!hasMounted) {
    return (
      <main className="relative bg-slate-50 min-h-screen">
        <div className="relative z-10 flex min-h-screen items-center justify-center">
          <LoadingSpinner size="lg" />
        </div>
      </main>
    );
  }

  return (
    <main className="relative bg-slate-50">
      {/* 3D Background (only if no reduced motion) */}
      {!prefersReducedMotion && (
        <div className="fixed inset-0 -z-10">
          <ThreeDBackground />
        </div>
      )}

      {/* Hero Content */}
      <div className="relative z-10 flex min-h-screen flex-col items-center justify-center px-6 py-24 text-center text-slate-900">
        <motion.h1 
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5 }}
          className="max-w-4xl text-4xl font-semibold tracking-tight text-slate-900 sm:text-6xl"
        >
          Architect. Automate. Accelerate.
        </motion.h1>
        
        <motion.p
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.2, duration: 0.5 }}
          className="mx-auto mt-6 max-w-2xl text-lg text-slate-600"
        >
          Enterprise-grade cloud, infrastructure, and software development — delivered with precision.
        </motion.p>

        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.4, duration: 0.5 }}
          className="mt-10"
        >
          <Button 
            size="lg" 
            onClick={() => setIsModalOpen(true)}
            aria-label="Open instant quote estimator"
            className="transition-transform hover:scale-105"
          >
            Get Your Free Architecture Review →
          </Button>
        </motion.div>
      </div>

      {/* Quote Estimator Modal */}
      <AnimatePresence>
        {isModalOpen && (
          <QuoteEstimatorModal onClose={() => setIsModalOpen(false)} />
        )}
      </AnimatePresence>
    </main>
  );
}