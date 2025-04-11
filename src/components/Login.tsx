import { useUser } from '../contexts/UserContext';

export function Login() {
  const { login } = useUser();

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault();
    // Add your authentication logic here
    // For example, make an API call to verify credentials
    
    const userData = {
      id: '123',
      email: 'user@example.com'
    };
    
    login(userData);
  };

  return (
    <form onSubmit={handleLogin}>
      {/* Your login form fields */}
    </form>
  );
} 