import { useUser } from '../contexts/UserContext';
import { Navigate } from 'react-router-dom';

export function ProtectedRoute({ children }: { children: React.ReactNode }) {
  const { user } = useUser();

  if (!user) {
    return <Navigate to="/login" />;
  }

  return <>{children}</>;
} 