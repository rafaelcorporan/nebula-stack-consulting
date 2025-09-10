'use client';

import { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { useForm } from 'react-hook-form';
import { z } from 'zod';
import { zodResolver } from '@hookform/resolvers/zod';
import { Button } from '@/components/ui/Button';
import { RadioGroup, RadioGroupItem } from '@/components/ui/RadioGroup';
import { Checkbox } from '@/components/ui/Checkbox';
import { Label } from '@/components/ui/Label';
import { Slider } from '@/components/ui/Slider';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/Select';

// Form Schema
const quoteSchema = z.object({
  service: z.string(),
  technologies: z.array(z.string()),
  scope: z.number().min(1).max(6),
  infra: z.string().optional(),
  name: z.string().min(1, "Name is required"),
  email: z.string().email("Valid email required"),
  company: z.string().min(1, "Company is required")
});

type QuoteForm = z.infer<typeof quoteSchema>;

// Pricing Config
const SERVICES = [
  { id: "cloud", label: "☁️ Cloud & AWS Architecture", basePrice: 5000 },
  { id: "iac", label: "🛠️ Terraform / Kubernetes", basePrice: 7000 },
  { id: "db", label: "🗃️ Database Setup & Migration", basePrice: 4000 },
  { id: "fullstack", label: "📱 Full-Stack Web + Mobile App", basePrice: 15000 },
  { id: "custom", label: "🚀 Custom Software Development", basePrice: 10000 }
];

const TECHNOLOGIES = [
  { id: "aws", label: "AWS (EC2, S3, Lambda)", addPrice: 3000 },
  { id: "terraform", label: "Terraform IaC", addPrice: 2500 },
  { id: "k8s", label: "Kubernetes Cluster", addPrice: 4000 },
  { id: "oracle", label: "Oracle DB", addPrice: 3500 },
  { id: "postgres", label: "PostgreSQL", addPrice: 2000 },
  { id: "mongodb", label: "MongoDB", addPrice: 2000 },
  { id: "react", label: "React/Next.js Frontend", addPrice: 5000 },
  { id: "ios", label: "iOS (Swift)", addPrice: 8000 },
  { id: "android", label: "Android (Kotlin)", addPrice: 8000 }
];

const INFRA_OPTIONS = [
  { id: "basic", label: "Basic (1 VPC, <10 instances)", addPrice: 0 },
  { id: "mid", label: "Mid (Multi-AZ, Load Balancer)", addPrice: 5000 },
  { id: "enterprise", label: "Enterprise (Global, Serverless, DR)", addPrice: 15000 }
];

const SCOPE_LABELS = [
  "1-2 weeks", "3-4 weeks", "1-2 months", "3-4 months", "5-6 months", "6+ months"
];

export function QuoteEstimatorModal({ onClose }: { onClose: () => void }) {
  const [step, setStep] = useState(1);
  const [showContact, setShowContact] = useState(false);
  const [estimatedPrice, setEstimatedPrice] = useState<number | null>(null);

  const { register, handleSubmit, watch, setValue, formState: { errors } } = useForm<QuoteForm>({
    resolver: zodResolver(quoteSchema),
    defaultValues: {
      technologies: [],
      scope: 3
    }
  });

  const formData = watch();

  // Calculate live estimate
  useEffect(() => {
    if (!formData.service) return;

    const service = SERVICES.find(s => s.id === formData.service);
    if (!service) return;

    let total = service.basePrice;

    // Add tech
    formData.technologies.forEach(techId => {
      const tech = TECHNOLOGIES.find(t => t.id === techId);
      if (tech) total += tech.addPrice;
    });

    // Multiply by scope
    total *= [1, 1.5, 2, 3, 4, 5][formData.scope - 1];

    // Add infra
    if (formData.infra) {
      const infra = INFRA_OPTIONS.find(i => i.id === formData.infra);
      if (infra) total += infra.addPrice;
    }

    setEstimatedPrice(Math.round(total / 500) * 500);
  }, [formData]);

  const onSubmit = (data: QuoteForm) => {
    console.log("Quote submitted:", data);
    // TODO: POST to /api/quote → Airtable/Zapier
    alert("Quote submitted! We’ll email your PDF summary.");
    onClose();
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/50 p-4 backdrop-blur-sm">
      <motion.div
        initial={{ opacity: 0, scale: 0.95 }}
        animate={{ opacity: 1, scale: 1 }}
        exit={{ opacity: 0, scale: 0.95 }}
        className="w-full max-w-3xl rounded-2xl bg-white p-8 shadow-2xl"
      >
        <div className="flex items-center justify-between">
          <h2 className="text-2xl font-bold text-slate-900">
            {showContact ? "Almost Done!" : "Get Your Instant Quote"}
          </h2>
          <button 
            onClick={onClose}
            className="rounded-full p-2 hover:bg-slate-100"
            aria-label="Close modal"
          >
            ✕
          </button>
        </div>

        {!showContact && estimatedPrice && (
          <div className="mt-4 rounded-lg bg-emerald-50 p-4 text-center">
            <p className="text-3xl font-bold text-emerald-700">${estimatedPrice.toLocaleString()}</p>
            <p className="text-sm text-slate-600">Estimated investment</p>
          </div>
        )}

        <form onSubmit={handleSubmit(onSubmit)} className="mt-6 space-y-6">
          {!showContact && step === 1 && (
            <div>
              <h3 className="text-lg font-semibold">1. What service do you need?</h3>
              <RadioGroup onValueChange={(v) => setValue('service', v)} className="mt-4 grid grid-cols-1 gap-3 sm:grid-cols-2">
                {SERVICES.map((service) => (
                  <div key={service.id}>
                    <RadioGroupItem value={service.id} id={service.id} className="peer sr-only" />
                    <Label
                      htmlFor={service.id}
                      className="flex cursor-pointer flex-col space-y-2 rounded-lg border-2 border-slate-200 p-4 text-sm peer-data-[state=checked]:border-sky-500 peer-data-[state=checked]:bg-sky-50"
                    >
                      {service.label}
                    </Label>
                  </div>
                ))}
              </RadioGroup>
              {errors.service && <p className="text-sm text-red-600">{errors.service.message}</p>}
              <div className="mt-6 flex justify-end">
                <Button 
                  type="button" 
                  onClick={() => setStep(2)} 
                  disabled={!formData.service}
                >
                  Next →
                </Button>
              </div>
            </div>
          )}

          {!showContact && step === 2 && (
            <div>
              <h3 className="text-lg font-semibold">2. Which technologies?</h3>
              <div className="mt-4 grid grid-cols-1 gap-3 sm:grid-cols-2">
                {TECHNOLOGIES.map((tech) => (
                  <div key={tech.id} className="flex items-center space-x-3">
                    <Checkbox 
                      id={tech.id} 
                      onCheckedChange={(checked) => {
                        const current = formData.technologies || [];
                        if (checked) {
                          setValue('technologies', [...current, tech.id]);
                        } else {
                          setValue('technologies', current.filter(t => t !== tech.id));
                        }
                      }}
                    />
                    <Label htmlFor={tech.id} className="text-sm">{tech.label}</Label>
                  </div>
                ))}
              </div>
              <div className="mt-6 flex justify-between">
                <Button type="button" variant="outline" onClick={() => setStep(1)}>
                  ← Back
                </Button>
                <Button type="button" onClick={() => setStep(3)}>
                  Next →
                </Button>
              </div>
            </div>
          )}

          {!showContact && step === 3 && (
            <div>
              <h3 className="text-lg font-semibold">3. Project scope?</h3>
              <div className="mt-4 space-y-4">
                <Slider
                  defaultValue={[3]}
                  max={6}
                  step={1}
                  onValueChange={(v) => setValue('scope', v[0])}
                  className="w-full"
                />
                <div className="flex justify-between text-xs text-slate-500">
                  {SCOPE_LABELS.map((label, i) => (
                    <span key={i}>{label}</span>
                  ))}
                </div>
              </div>
              <div className="mt-6 flex justify-between">
                <Button type="button" variant="outline" onClick={() => setStep(2)}>
                  ← Back
                </Button>
                <Button 
                  type="button" 
                  onClick={() => {
                    if (['cloud', 'iac'].includes(formData.service || '')) {
                      setStep(4);
                    } else {
                      setShowContact(true);
                    }
                  }}
                >
                  {['cloud', 'iac'].includes(formData.service || '') ? 'Next →' : 'See Quote →'}
                </Button>
              </div>
            </div>
          )}

          {!showContact && step === 4 && (
            <div>
              <h3 className="text-lg font-semibold">4. Infrastructure scale?</h3>
              <Select onValueChange={(v) => setValue('infra', v)}>
                <SelectTrigger className="mt-4 w-full">
                  <SelectValue placeholder="Select infrastructure scale" />
                </SelectTrigger>
                <SelectContent>
                  {INFRA_OPTIONS.map((opt) => (
                    <SelectItem key={opt.id} value={opt.id}>{opt.label}</SelectItem>
                  ))}
                </SelectContent>
              </Select>
              <div className="mt-6 flex justify-between">
                <Button type="button" variant="outline" onClick={() => setStep(3)}>
                  ← Back
                </Button>
                <Button type="button" onClick={() => setShowContact(true)}>
                  See Quote →
                </Button>
              </div>
            </div>
          )}

          {showContact && (
            <div>
              <h3 className="text-lg font-semibold">Unlock your full quote</h3>
              <p className="mt-2 text-sm text-slate-600">We’ll email you a PDF summary + schedule options.</p>
              
              <div className="mt-6 space-y-4">
                <div>
                  <Label htmlFor="name">Name</Label>
                  <input 
                    id="name" 
                    {...register('name')} 
                    className="mt-1 w-full rounded-lg border border-slate-300 px-3 py-2"
                  />
                  {errors.name && <p className="text-sm text-red-600">{errors.name.message}</p>}
                </div>
                
                <div>
                  <Label htmlFor="email">Email</Label>
                  <input 
                    id="email" 
                    type="email" 
                    {...register('email')} 
                    className="mt-1 w-full rounded-lg border border-slate-300 px-3 py-2"
                  />
                  {errors.email && <p className="text-sm text-red-600">{errors.email.message}</p>}
                </div>
                
                <div>
                  <Label htmlFor="company">Company</Label>
                  <input 
                    id="company" 
                    {...register('company')} 
                    className="mt-1 w-full rounded-lg border border-slate-300 px-3 py-2"
                  />
                  {errors.company && <p className="text-sm text-red-600">{errors.company.message}</p>}
                </div>
              </div>

              <div className="mt-8 flex justify-between">
                <Button type="button" variant="outline" onClick={() => setShowContact(false)}>
                  ← Back
                </Button>
                <Button type="submit">
                  Get My Quote PDF →
                </Button>
              </div>
            </div>
          )}
        </form>
      </motion.div>
    </div>
  );
}

export default QuoteEstimatorModal;